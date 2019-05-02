import { Component, Input, OnInit } from '@angular/core';
import { Http } from '@angular/http';
import { Title } from '@angular/platform-browser';
import { Router } from '@angular/router';
import { DialogService } from '../../services/dialog.service';

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
    private http: Http,
    private router: Router,
    private title: Title,
    private dialog: DialogService,
  ) {}

  public ngOnInit() {
    this.title.setTitle('ログイン');
  }

  public login() {
    this.http
      .post('/api/login', {
        account: this.account,
        password: this.password,
      })
      .subscribe(
        res => {
          localStorage.setItem('ACCESS_TOKEN', res.json().token);
          this.router.navigate(['cuisine']);
        },
        err => {
          const errors = err.json().message;
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
