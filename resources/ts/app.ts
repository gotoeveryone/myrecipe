import 'reflect-metadata';
import 'zone.js/dist/zone';
import 'rxjs/Rx';

import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';

import { NgModule, enableProdMode } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule, Http, XHRBackend, RequestOptions } from '@angular/http';

import { Cuisine, CuisineHeader, CuisineItems } from './cuisine/cuisine';
import { Colorbox } from './components/colorbox';
import { Dialog } from './components/dialog';
import { CustomHttp } from './components/customhttp';

export const WEB_ROOT = '/recipe/';

declare const PRODUCTION: boolean;

if (PRODUCTION) {
    enableProdMode();
}

@NgModule({
    imports: [
        BrowserModule,
        HttpModule,
        FormsModule,
    ],
    providers: [
        {
            provide: Http,
            useFactory: (backend: XHRBackend, options: RequestOptions) => {
                return new CustomHttp(backend, options);
            },
            deps: [XHRBackend, RequestOptions],
        },
    ],
    declarations: [
        Dialog,
        Colorbox,
        Cuisine,
        CuisineHeader,
        CuisineItems,
    ],
    bootstrap: [
        Cuisine,
    ]
})
export class AppModule { }

platformBrowserDynamic().bootstrapModule(AppModule);
