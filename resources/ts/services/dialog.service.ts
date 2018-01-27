import { Injectable } from '@angular/core';

/**
 * ダイアログ制御サービス
 */
@Injectable()
export class DialogService {
    private _title = 'タイトル';
    private _message = '';
    private _error = false;

    open(title = '', message = '', error = false) {
        this._title = title;
        this._message = message;
        this._error = error;
    }

    close() {
        this._title = '';
        this._message = '';
        this._error = false;
    }

    get error() {
        return this._error;
    }

    get title() {
        return this._title;
    }

    get message() {
        return this._message;
    }
}
