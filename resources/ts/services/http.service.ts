import { Observable } from 'rxjs/Observable';
import { Injectable } from '@angular/core';
import {
    Http, Headers, ConnectionBackend, Request, Response,
    RequestOptions, RequestOptionsArgs
} from '@angular/http';
import { BlockUIService } from './blockui.service';

/**
 * カスタムHTTPモジュール
 */
@Injectable()
export class MyHttp extends Http { 
    constructor(backend: ConnectionBackend, defaultOptions: RequestOptions, private blockUI: BlockUIService) {
        super(backend, defaultOptions);
    }

    request(url: string | Request, options?: RequestOptionsArgs): Observable<Response> {
        this.blockUI.block();
        return super.request(url, options).finally(() => {
            this.blockUI.unBlock();
        });
    }

    post(url: string, body: any, options?: RequestOptionsArgs): Observable<Response> {
        return super.post(url, body, this.withGeneralHeaders(options));
    }

    put(url: string, body: any, options?: RequestOptionsArgs): Observable<Response> {
        return super.put(url, body, this.withGeneralHeaders(options));
    }

    private withGeneralHeaders(options?: RequestOptionsArgs): RequestOptionsArgs {
        if (!options) {
            options = new RequestOptions({
                headers: new Headers(),
            });
        }
        const accessUser = document.querySelector('[name=accessUser').getAttribute('value');
        const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').getAttribute('value');
        options.headers.set('X-Access-User', accessUser);
        options.headers.set('X-CSRFToken', csrfToken);

        return options;
    }
}