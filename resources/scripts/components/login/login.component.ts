import { Component, Input, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Title } from '@angular/platform-browser';
import { Router } from '@angular/router';
import { DialogService } from '../../services/dialog.service';
import { Token } from '../../types';

declare var require: any;

/**
 * ログインコンポーネント
 */
@Component({
  selector: '[login]',
  template: require('./login.component.html'),
})
export class LoginComponent implements OnInit {
  @Input() public account: string;
  @Input() public password: string;

  public constructor(
    private http: HttpClient,
    private router: Router,
    private title: Title,
    private dialog: DialogService,
  ) {}

  public ngOnInit() {
    this.title.setTitle('ログイン');
  }

  public login() {
    this.http
      .post<Token>('/api/login', {
      account: this.account,
      password: this.password,
    })
      .subscribe(
        res => {
          localStorage.setItem('ACCESS_TOKEN', res.token);
          this.router.navigate(['cuisine']);
        },
        err => {
          const errors = err.error.message;
          if (err.status !== 400) {
            this.dialog.open('エラー', errors, true);
          } else {
            const messages = Array.prototype.concat.apply(
              [],
              Object.keys(errors).map((key: string) =>
                errors[key].map((message: string) => `${key}:${message}`),
              ),
            );
            this.dialog.open('エラー', messages, true);
          }
        },
      );
  }
}
