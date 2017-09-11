import 'reflect-metadata';
import 'zone.js/dist/zone';
import 'rxjs/Rx';

import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { NgModule, enableProdMode } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule, Http, XHRBackend, RequestOptions, XSRFStrategy, CookieXSRFStrategy } from '@angular/http';
import { RouterModule, PreloadAllModules } from '@angular/router';

import { ROUTES } from './routes';
import { MyHttp } from './services/http.service';
import { BlockUIService } from './services/blockui.service';
import { DialogService } from './services/dialog.service';
import { MyRequestOptions } from './services/request.service';

import { AppComponent } from './app.component';
import { Dialog } from './components/parts/dialog.component';
import { SearchComponent } from './components/cuisine-list/cuisine.component';
import { HeaderComponent } from './components/cuisine-list/header.component';
import { ItemComponent } from './components/cuisine-list/item.component';
import { DetailComponent } from './components/cuisine-detail/detail.component';
import { InstructionComponent } from './components/cuisine-detail/instruction.component';
import { FoodstuffComponent } from './components/cuisine-detail/foodstuff.component';

declare const PRODUCTION: boolean;

if (PRODUCTION) {
    enableProdMode();
}

@NgModule({
    imports: [
        BrowserModule,
        HttpModule,
        FormsModule,
        ReactiveFormsModule,
        RouterModule.forRoot(ROUTES, { useHash: true, /*preloadingStrategy: PreloadAllModules*/ })
    ],
    providers: [
        {
            provide: Http,
            useFactory: (backend: XHRBackend, options: RequestOptions, blockUI: BlockUIService) => {
                return new MyHttp(backend, options, blockUI);
            },
            deps: [XHRBackend, RequestOptions, BlockUIService],
        },
        {
            provide: XSRFStrategy,
            useValue: new CookieXSRFStrategy('csrftoken', 'X-CSRFToken'),
        },
        {
            provide: RequestOptions,
            useClass: MyRequestOptions,
        },
        BlockUIService,
        DialogService,
    ],
    declarations: [
        AppComponent,
        Dialog,
        SearchComponent,
        HeaderComponent,
        ItemComponent,
        DetailComponent,
        InstructionComponent,
        FoodstuffComponent,
    ],
    bootstrap: [
        AppComponent,
    ]
})
export class AppModule { }

platformBrowserDynamic().bootstrapModule(AppModule);
