import { Component, Input } from '@angular/core';
import { NgIf, NgForOf, NgClass } from '@angular/common';
import { NgModel } from '@angular/forms';

declare var require: any;

/**
 * 食材コンポーネント
 */
@Component({
    selector: '[foodstuffs]',
    template: require('./foodstuff.component.html'),
})
export class FoodstuffComponent {
    @Input() items: any[];

    addRow() {
        this.items.push({});
    }

    deleteRow() {
        this.items.pop();
    }
}
