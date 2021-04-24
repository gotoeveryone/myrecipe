import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { Classification } from '../../types';

declare let require: any;

/**
 * ヘッダ出力コンポーネント
 */
@Component({
  selector: '[cuisine-header]',
  template: require('./header.component.html'),
})
export class HeaderComponent implements OnInit {
  @Output() public onSearch = new EventEmitter<any>();

  public types = [] as any[];
  public name = '';
  public classification = '';
  public kcal = '';

  public constructor(private http: HttpClient, private router: Router) {}

  /**
   * 値変更時
   *
   * @param {any} $event
   */
  public changeValue($event: any) {
    this.onSearch.emit({
      [$event.target.name]: $event.target.value,
    });
  }

  /**
   * 追加画面へ
   */
  public toAdd() {
    this.router.navigate(['cuisine/new']);
  }

  /**
   * {@inheritdoc}
   */
  public ngOnInit() {
    // 初期表示時に検索する
    this.http.get<Classification[]>('/api/classifications').subscribe(res => {
      this.types = res;
      this.onSearch.emit();
    });
  }
}
