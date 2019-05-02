import { Component, OnInit } from '@angular/core';
import { Http } from '@angular/http';
import { Title } from '@angular/platform-browser';
import { ActivatedRoute, Router } from '@angular/router';
import { DialogService } from '../../services/dialog.service';

declare var require: any;

/**
 * レシピ詳細コンポーネント
 */
@Component({
  selector: '.content-inner',
  template: require('./detail.component.html'),
})
export class DetailComponent implements OnInit {
  public items = [] as any[];
  public params = new Object();
  public cuisineId: number;
  public cuisine = {
    instructions: [] as any[],
    foodstuffs: [] as any[],
  };
  public types = [] as any[];
  public dataList: string[];

  public constructor(
    private http: Http,
    private router: Router,
    private route: ActivatedRoute,
    private title: Title,
    private dialog: DialogService,
  ) {}

  public toSearch() {
    this.router.navigate(['cuisine']);
  }

  public getLabel() {
    return this.cuisineId ? '更新' : '登録';
  }

  /**
   * 保存処理
   */
  public save() {
    if (this.cuisineId) {
      this.http.put(this.getUrl('put'), this.cuisine).subscribe(
        res => {
          this.cuisine = res.json();
          this.dialog.open('メッセージ', 'レシピを更新しました。');
        },
        err => this.apiError(err),
      );
    } else {
      this.http.post(this.getUrl('post'), this.cuisine).subscribe(
        res => {
          this.cuisine = res.json();
          this.dialog.open('メッセージ', 'レシピを登録しました。');
        },
        err => this.apiError(err),
      );
    }
  }

  /**
   * レスポンスからエラーメッセージを生成
   *
   * @param err
   */
  public apiError(err: Response) {
    if (err.status !== 400) {
      this.dialog.open('エラー', 'エラーが発生しました。', true);
      return;
    }
    const errors = [] as string[];
    const obj = err.json();
    Object.keys(obj).forEach(k => {
      const values: any[] = obj[k] || [];
      values.forEach(v => {
        if (v instanceof Object) {
          Object.keys(v).forEach(ck => {
            errors.push(`${ck}: ${v[ck]}`);
          });
        } else {
          errors.push(`${k}: ${v}`);
        }
      });
    });
    this.dialog.open('エラー', errors, true);
  }

  /**
   * {@inheritDoc}
   */
  public ngOnInit() {
    // 初期表示時に検索する
    this.http.get('/api/classifications').subscribe(res => {
      this.types = res.json();
      // パラメータからIDを取得
      this.route.params.subscribe(params => {
        this.cuisineId = params['id'];

        if (!this.cuisineId) {
          this.title.setTitle('レシピ登録');
          for (let i = 0; i < 3; i++) {
            this.cuisine.instructions.push({
              sort_order: i + 1,
            });
            this.cuisine.foodstuffs.push({});
          }
        } else {
          this.title.setTitle('レシピ編集');
          this.http.get(this.getUrl('get')).subscribe(res => (this.cuisine = res.json()));
        }

        // 食材の補完情報を取得
        this.http.get('/api/foodstuffs/').subscribe(res => (this.dataList = res.json()));
      });
    });
  }

  /**
   * 対象APIのURLを取得
   *
   * @private
   * @param _type
   */
  private getUrl(_type: string) {
    switch (_type.toUpperCase()) {
      case 'GET':
      case 'PUT':
      case 'DELETE':
        return `/api/cuisine/${this.cuisineId}/`;
      case 'POST':
        return '/api/cuisine/';
    }
    return '';
  }
}
