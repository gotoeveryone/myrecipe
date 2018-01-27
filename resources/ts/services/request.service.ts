import { Injectable } from '@angular/core';
import { BaseRequestOptions } from '@angular/http';

declare var window: any;
window.Django = window.Django || {};

@Injectable()
export class MyRequestOptions extends BaseRequestOptions {
    constructor() {
        super();
        this.headers.set('X-USERID', window.Django.userId);
    }
}
