import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Title } from '@angular/platform-browser';
import { ActivatedRoute, Router } from '@angular/router';
import { Classification, Cuisine, Foodstuff, Instruction } from '../../types';
import { DialogService } from '../../services/dialog.service';

declare const require: any;

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
    instructions: [] as Instruction[],
    foodstuffs: [] as Foodstuff[],
  };
  public types = [] as Classification[];
  public dataList: string[];

  public constructor(
    private http: HttpClient,
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
      this.http.put<Cuisine>(this.getUrl('put'), this.cuisine).subscribe(
        res => {
          this.cuisine = res;
          this.dialog.open('メッセージ', 'レシピを更新しました。');
        },
        err => this.apiError(err),
      );
    } else {
      this.http.post<Cuisine>(this.getUrl('post'), this.cuisine).subscribe(
        res => {
          this.cuisine = res;
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
  public apiError(err: any) {
    if (err.status !== 400) {
      this.dialog.open('エラー', 'エラーが発生しました。', true);
      return;
    }
    const errors = [] as string[];
    const obj = err.error;
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
    this.http.get<Classification[]>('/api/classifications').subscribe(res => {
      this.types = res;
      // パラメータからIDを取得
      this.route.params.subscribe(params => {
        this.cuisineId = params['id'];

        if (!this.cuisineId) {
          this.title.setTitle('レシピ登録');
          for (let i = 0; i < 3; i++) {
            this.cuisine.instructions.push({
              sort_order: i + 1,
            });
            this.cuisine.foodstuffs.push({} as unknown as Foodstuff);
          }
        } else {
          this.title.setTitle('レシピ編集');
          this.http.get<Cuisine>(this.getUrl('get')).subscribe(res => (this.cuisine = res));
        }

        // 食材の補完情報を取得
        this.http.get<string[]>('/api/foodstuffs/').subscribe(res => (this.dataList = res));
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
