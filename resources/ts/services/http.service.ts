import { Observable } from 'rxjs/Observable';
import { Injectable } from '@angular/core';
import {
    Http, ConnectionBackend, Request, Response,
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
}
