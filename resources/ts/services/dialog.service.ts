import { Injectable } from '@angular/core';

/**
 * ダイアログ制御サービス
 */
@Injectable()
export class DialogService {
    private _title: String = 'タイトル';
    private _message: String = '';
    private _error: Boolean = false;

    open(title: String = '', message: String = '', error: Boolean = false) {
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
