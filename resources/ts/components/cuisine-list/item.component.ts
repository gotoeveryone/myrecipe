import { Component, Input } from '@angular/core';
import { Http } from '@angular/http';
import { Router } from '@angular/router';
import { DialogService } from '../../services/dialog.service';

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

    constructor(
        private http: Http,
        private router: Router,
        private dialog: DialogService,
    ) { }

    /**
     * 詳細画面表示
     *
     * @param {number} id
     * @return void
     */
    detailUrl(id: number): void {
        this.router.navigate(['cuisine/', id]);
    }

    /**
     * メール送信URL取得
     *
     * @param id
     */
    notice(id: number) {
        this.http.post('/api/notice', { id })
            .subscribe(
                (_) => this.dialog.open('メッセージ', 'メールを送信しました。'),
                (_) => this.dialog.open('エラー', 'メール送信に失敗しました。', true),
            );
    }
}
