import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import {
    CookieXSRFStrategy,
    Http,
    HttpModule,
    RequestOptions,
    XHRBackend,
    XSRFStrategy,
} from '@angular/http';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';

import { ROUTES } from './routes';
import { AuthGuardService } from './services/auth.service';
import { BlockUIService } from './services/blockui.service';
import { DialogService } from './services/dialog.service';
import { MyHttp } from './services/http.service';
import { MyRequestOptions } from './services/request.service';

import { AppComponent } from './app.component';
import { DetailComponent } from './components/cuisine-detail/detail.component';
import { FoodstuffComponent } from './components/cuisine-detail/foodstuff.component';
import { InstructionComponent } from './components/cuisine-detail/instruction.component';
import { SearchComponent } from './components/cuisine-list/cuisine.component';
import { HeaderComponent } from './components/cuisine-list/header.component';
import { ItemComponent } from './components/cuisine-list/item.component';
import { LoginComponent } from './components/login/login.component';
import { NotFoundComponent } from './components/not-found/not-found.component';
import { Dialog } from './components/parts/dialog.component';
import { Header } from './components/parts/header.component';

@NgModule({
    imports: [
        BrowserModule,
        HttpModule,
        FormsModule,
        ReactiveFormsModule,
        RouterModule.forRoot(ROUTES, { useHash: true }),
    ],
    providers: [
        {
            provide: Http,
            useFactory: (
                backend: XHRBackend,
                options: RequestOptions,
                blockUI: BlockUIService
            ) => {
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
        AuthGuardService,
        BlockUIService,
        DialogService,
    ],
    declarations: [
        AppComponent,
        Dialog,
        Header,
        NotFoundComponent,
        LoginComponent,
        SearchComponent,
        HeaderComponent,
        ItemComponent,
        DetailComponent,
        InstructionComponent,
        FoodstuffComponent,
    ],
    bootstrap: [AppComponent, Header],
})
export class AppModule {}
