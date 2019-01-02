import { Injectable } from '@angular/core';

/**
 * ダイアログ制御サービス
 */
@Injectable()
export class DialogService {
    private _title = 'タイトル';
    private _messages = new Array();
    private _error = false;

    open(title = '', messages: string | string[] = '', error = false) {
        this._title = title;
        if (!Array.isArray(messages)) {
            messages = [messages];
        }
        this._messages = messages;
        this._error = error;
    }

    close() {
        this._title = '';
        this._messages = new Array();
        this._error = false;
    }

    get error() {
        return this._error;
    }

    get title() {
        return this._title;
    }

    get messages() {
        return this._messages;
    }
}
