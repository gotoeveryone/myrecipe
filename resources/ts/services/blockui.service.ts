import { Injectable } from '@angular/core';

/**
 * 画面のブロックを制御するためのサービス
 */
@Injectable()
export class BlockUIService {
    private _blocked = true;

    get blocked() {
        return this._blocked;
    }

    block() {
        this._blocked = true;
    }

    unBlock() {
        this._blocked = false;
    }
}
