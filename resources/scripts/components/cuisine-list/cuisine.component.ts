import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Title } from '@angular/platform-browser';
import { Cuisine} from '../../types';

declare var require: any;

/**
 * レシピ検索コンポーネント
 */
@Component({
  selector: '.content-inner',
  template: require('./cuisine.component.html'),
})
export class SearchComponent implements OnInit {
  public items = [] as any[];
  public params = new Object();

  public constructor(private http: HttpClient, private title: Title) {}

  /**
   * {@inheritdoc}
   */
  public ngOnInit() {
    this.title.setTitle('レシピ検索');
  }

  /**
   * 検索処理
   *
   * @param {any} _params
   */
  public search(_params: {
    [param: string]: string | string[];
  } = {}) {
    Object.keys(_params).forEach(key => {
      this.params[key] = _params[key];
    });

    this.http.get<Cuisine[]>('/api/cuisine/', {
      params: this.params as any,
    }).forEach(res => {
      this.items = res;
    });
  }
}
