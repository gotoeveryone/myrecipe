import { Injectable } from '@angular/core';
import { BaseRequestOptions, RequestOptions, RequestOptionsArgs } from '@angular/http';

@Injectable()
export class MyRequestOptions extends BaseRequestOptions {
    constructor() {
        super();
    }

    merge(options?: RequestOptionsArgs): RequestOptions {
        const newOptions = super.merge(options);
        newOptions.headers.set('Authorization', `Bearer ${localStorage.getItem('ACCESS_TOKEN')}`);
        return newOptions;
    }
}
