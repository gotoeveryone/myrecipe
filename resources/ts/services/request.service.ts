import { Injectable } from '@angular/core';
import { BaseRequestOptions } from '@angular/http';

declare global {
    interface Window {
        Django: any;
    }
}

// declare var window: Window;

@Injectable()
export class MyRequestOptions extends BaseRequestOptions {
    constructor() {
        super();
        this.headers.set('X-USERID', window.Django.userId);
    }
}
