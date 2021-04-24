import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Title } from '@angular/platform-browser';
import { Router } from '@angular/router';
import { AuthGuardService } from '../../services/auth.service';

declare let require: any;

/**
 * ヘッダを表示するためのコンポーネント
 */
@Component({
  selector: '.header',
  template: require('./header.component.html'),
})
export class Header {
  private opened = false;

  public constructor(
    private http: HttpClient,
    private router: Router,
    private auth: AuthGuardService,
    private title: Title,
  ) {}

  public getTitle() {
    return this.title.getTitle();
  }

  public logout() {
    this.http.delete('/api/logout').subscribe(() => {
      localStorage.removeItem('ACCESS_TOKEN');
      this.auth.clearUser();
      this.router.navigate(['/']);
    });
  }

  public toggleMenu() {
    this.opened = !this.opened;
  }

  public get userNameAndEmail() {
    const user = this.auth.getUser();
    if (user.name) {
      return `${user.name} (${user.email})`;
    }
    return `${user.account} (${user.email})`;
  }
}
