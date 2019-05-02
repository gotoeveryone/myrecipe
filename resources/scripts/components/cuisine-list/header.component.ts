import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { Http } from '@angular/http';
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
  @Output() public onSearch = new EventEmitter<any>();

  public types = [] as any[];
  public name = '';
  public classification = '';
  public kcal = '';

  public constructor(private http: Http, private router: Router) {}

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
    this.http.get('/api/classifications').subscribe(res => {
      this.types = res.json();
      this.onSearch.emit();
    });
  }
}
