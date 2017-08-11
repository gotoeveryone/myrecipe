import { Component, Input } from '@angular/core';
import { NgIf, NgFor, NgClass } from '@angular/common';
import { NgModel } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { WEB_ROOT } from '../../const';

declare var require: any;

/**
 * データ出力コンポーネント
 */
@Component({
    selector: '[cuisine-items]',
    template: require('./item.component.html'),
})
export class ItemComponent {
    @Input() items: any[];

    constructor(private router: Router) { }

    /**
     * 詳細画面表示
     * 
     * @param {number} id
     * @return void
     */
    detailUrl(id: number): void {
        this.router.navigate(['/edit/', id]);
    }

    /**
     * メール送信URL取得
     * 
     * @param {number} id
     * @return {string} URL
     */
    noticeUrl(id: number) {
        return `${WEB_ROOT}/cuisine/notice/${id}`;
    }
}
