import { Component, Input } from '@angular/core';
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
    @Input() messages: string[];

    constructor(private dialog: DialogService) { }

    isShow() {
        return this.dialog.messages && this.dialog.messages.length;
    }
}
