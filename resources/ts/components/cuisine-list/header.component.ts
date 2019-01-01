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
    @Output() onSearch = new EventEmitter<any>();

    types = new Array();
    name = '';
    classification = '';
    kcal = '';

    constructor(
        private http: Http,
        private router: Router,
    ) { }

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
     * 追加画面へ
     */
    toAdd() {
        this.router.navigate(['/add']);
    }

    /**
     * {@inheritdoc}
     */
    ngOnInit() {
        // 初期表示時に検索する
        this.http.get('/api/classifications')
            .subscribe((res) => {
                this.types = res.json();
                this.onSearch.emit();
            });
    }
}
