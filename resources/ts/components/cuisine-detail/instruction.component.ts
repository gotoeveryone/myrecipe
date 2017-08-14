import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core';
import { Http, Headers, RequestOptions, URLSearchParams } from '@angular/http';
import { NgIf, NgFor, NgClass } from '@angular/common';
import { NgModel } from '@angular/forms';

declare var require: any;

/**
 * 調理手順コンポーネント
 */
@Component({
    selector: '[instructions]',
    template: require('./instruction.component.html'),
})
export class InstructionComponent {
    @Input() items: any[];

    addRow() {
        this.items.push({});
    }

    deleteRow() {
        this.items.pop();
    }

    getOrder(_item: any) {
        if (!_item.sort_order) {
            _item.sort_order = this.items.length;
        }
        return `${_item.sort_order}：`;
    }
}
