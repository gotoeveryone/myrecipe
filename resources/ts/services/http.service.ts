import { Injectable } from '@angular/core';
import {
    ConnectionBackend, Http, Request,
    RequestOptions, RequestOptionsArgs, Response,
} from '@angular/http';
import { Observable } from 'rxjs/Observable';
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
