import { Component, OnInit } from '@angular/core';
import { Http, RequestOptions } from '@angular/http';
import { Title } from '@angular/platform-browser';

declare var require: any;

/**
 * レシピ検索コンポーネント
 */
@Component({
    selector: '.content-inner',
    template: require('./cuisine.component.html'),
})
export class SearchComponent implements OnInit {
    items = new Array();
    params = new Object();

    constructor(
        private http: Http,
        private title: Title,
    ) { }

    /**
     * {@inheritdoc}
     */
    ngOnInit() {
        this.title.setTitle('レシピ検索');
    }

    /**
     * 検索処理
     *
     * @param {any} _params
     */
    search(_params: any = {}) {
        Object.keys(_params).forEach((key) => {
            this.params[key] = _params[key];
        });

        this.http.get('/api/cuisine/', new RequestOptions({ search: this.params }))
            .forEach((res) => {
                this.items = res.json();
            });
    }
}
