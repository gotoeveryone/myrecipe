import { Injectable } from '@angular/core';

/**
 * ダイアログ制御サービス
 */
@Injectable()
export class DialogService {
  private _title = 'タイトル';
  private _messages = [] as string[];
  private _error = false;

  public open(title = '', messages: string | string[] = '', error = false) {
    this._title = title;
    if (!Array.isArray(messages)) {
      messages = [messages];
    }
    this._messages = messages;
    this._error = error;
  }

  public close() {
    this._title = '';
    this._messages = [];
    this._error = false;
  }

  public get error() {
    return this._error;
  }

  public get title() {
    return this._title;
  }

  public get messages() {
    return this._messages;
  }
}
