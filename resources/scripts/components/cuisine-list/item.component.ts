import { Component, Input } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { DialogService } from '../../services/dialog.service';

declare let require: any;

/**
 * データ出力コンポーネント
 */
@Component({
  selector: '[cuisine-items]',
  template: require('./item.component.html'),
})
export class ItemComponent {
  @Input() public items: any[];

  public constructor(private http: HttpClient, private router: Router, private dialog: DialogService) {}

  /**
   * 詳細画面表示
   *
   * @param {number} id
   * @return void
   */
  public detailUrl(id: number): void {
    this.router.navigate(['cuisine/', id]);
  }

  /**
   * メール送信URL取得
   *
   * @param id
   */
  public notice(id: number) {
    this.http
      .post('/api/notice', { id })
      .subscribe(
        () => this.dialog.open('メッセージ', 'メールを送信しました。'),
        () => this.dialog.open('エラー', 'メール送信に失敗しました。', true),
      );
  }
}
