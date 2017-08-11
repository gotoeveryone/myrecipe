import { Component, Input, Output, EventEmitter } from '@angular/core';
import { DialogService } from '../../services/dialog.service';

declare var require: any;

/**
 * ダイアログを表示するためのコンポーネント
 */
@Component({
    selector: '[dialog]',
    template: require('./dialog.component.html'),
})
export class Dialog {
    constructor(private dialog: DialogService) { }
}
