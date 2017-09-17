import { Component } from '@angular/core';
import { Http, RequestOptions } from '@angular/http';
import { NgIf, NgFor, NgClass } from '@angular/common';
import { NgModel } from '@angular/forms';
import { WEB_ROOT } from '../../const';

declare var require: any;

/**
 * レシピ検索コンポーネント
 */
@Component({
    selector: '.content-inner',
    template: require('./cuisine.component.html'),
})
export class SearchComponent {
    items = new Array();
    params = new Object();

    constructor(private http: Http) { }

    /**
     * 検索処理
     *
     * @param {any} _params
     */
    search(_params: any = {}) {
        Object.keys(_params).forEach(key => {
            this.params[key] = _params[key];
        });

        this.http.get(`${WEB_ROOT}/api/cuisine/`, new RequestOptions({ search: this.params }))
            .forEach((res) => {
                this.items = res.json();
            });
    }
}
