import { Component, Input, Output, EventEmitter } from '@angular/core';
import { Http, Headers, RequestOptions, URLSearchParams } from '@angular/http';
import { NgIf, NgFor, NgClass } from '@angular/common';
import { NgModel } from '@angular/forms';
import { WEB_ROOT } from '../base';
import { Colorbox } from '../components/colorbox';

/**
 * タイトル情報検索コンポーネント
 */
@Component({
    selector: 'search-cuisine',
    template: `
        <div class="search-cuisine">
            <div cuisine-header (onSearch)="search($event)"></div>
            <div cuisine-items [items]="items"></div>
        </div>
    `,
})
export class Cuisine {
    items = new Array();
    params = new Object();

    constructor(private http: Http) { }

    /**
     * 検索処理
     * 
     * @param {any} _params
     */
    search(_params: any) {
        console.log(_params);
        Object.keys(_params).forEach(key => {
            this.params[key] = _params[key];
        });

        this.http.get(`${WEB_ROOT}api/cuisine/`, new RequestOptions({ search: this.params }))
            .forEach((res) => {
                this.items = res.json();
            });
    }
}

/**
 * ヘッダ出力コンポーネント
 */
@Component({
    selector: '[cuisine-header]',
    template: `
        <ul class="search-header">
            <li class="search-row">
                <label>名前：</label>
                <input type="text" name="name" ([ngModel])="name" (change)="changeValue($event)">
                <label>分類：</label>
                <select name="classification" ([ngModel])="classification" (change)="changeValue($event)" [ngModel]="classification">
                    <option *ngFor="let type of types" [value]="type" [innerText]="type"></option>
                </select>
                <label>カロリー：</label>
                <input type="text" name="kcal" ([ngModel])="kcal" (change)="changeValue($event)">以下
                <div class="button-wrap">
                    <button type="button" (click)="toAdd()">新規追加</button>
                </div>
            </li>
        </ul>
    `,
})
export class CuisineHeader {
    types = this.getTypes();
    @Output() onSearch = new EventEmitter<any>();

    name: string;
    classification: string;
    kcal: string;

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

/**
 * データ出力コンポーネント
 */
@Component({
    selector: '[cuisine-items]',
    template: `
        <div class="search-results">
            <ul class="table-header">
                <li class="table-row">
                    <span class="name">メニュー</span>
                    <span class="type">分類</span>
                    <span class="kcal">Kcal</span>
                    <span class="count">作成回数</span>
                    <span class="detail-link">詳細</span>
                </li>
            </ul>
            <ul class="table-body" *ngIf="items.length">
                <li class="table-row" *ngFor="let item of items">
                    <span class="name" [innerText]="item.name"></span>
                    <span class="type" [innerText]="item.classification"></span>
                    <span class="kcal" [innerText]="item.ingestion_kcal"></span>
                    <span class="count" [innerText]="item.create_number_of_times"></span>
                    <span class="detail-link">
                        <a class="button" [href]="detailUrl(item.id)">詳細を見る</a>
                        <a class="button" [href]="noticeUrl(item.id)">メール送信</a>
                    </span>
                </li>
            </ul>
        </div>
    `,
})
export class CuisineItems {
    @Input() items: any[];

    constructor(private http: Http) { }

    /**
     * 詳細URL取得
     * 
     * @param {number} id
     * @return {string} URL
     */
    detailUrl(id: number) {
        return `/recipe/cuisine/edit/${id}`;
    }

    /**
     * メール送信URL取得
     * 
     * @param {number} id
     * @return {string} URL
     */
    noticeUrl(id: number) {
        return `/recipe/cuisine/notice/${id}`;
    }
}
