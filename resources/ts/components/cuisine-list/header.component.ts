import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { Router } from '@angular/router';

declare var require: any;

/**
 * ヘッダ出力コンポーネント
 */
@Component({
    selector: '[cuisine-header]',
    template: require('./header.component.html'),
})
export class HeaderComponent implements OnInit {
    types = this.getTypes();
    @Output() onSearch = new EventEmitter<any>();

    name = '';
    classification = '';
    kcal = '';

    constructor(private router: Router) { }

    /**
     * 値変更時
     *
     * @param {any} $event
     */
    changeValue($event: any) {
        this.onSearch.emit({
            [$event.target.name]: $event.target.value,
        });
    }

    /**
     * 追加画面へ
     */
    toAdd() {
        this.router.navigate(['/add']);
    }

    /**
     * {@inheritdoc}
     */
    ngOnInit() {
        // 初期表示時に検索する
        this.onSearch.emit();
    }

    /**
     * 分類一覧取得
     *
     * @private
     * @return {Array} 分類一覧
     */
    private getTypes() {
        return [
            '', '主菜', '副菜', '主食', 'デザート', 'その他',
        ];
    }
}
