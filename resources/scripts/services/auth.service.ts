import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CanActivate, Router } from '@angular/router';

interface User {
  account: string;
  name: string;
  email: string;
}

/**
 * 認証状態をチェックするためのサービス
 */
@Injectable()
export class AuthGuardService implements CanActivate {
  private user: User;

  public constructor(private http: HttpClient, private router: Router) {}

  public getUser() {
    return this.user;
  }

  public clearUser() {
    this.user = null;
  }

  public hasUser() {
    return this.user && this.user.account.length > 0;
  }

  public async canActivate(): Promise<boolean> {
    const logged = await this.isAuthenticated();
    if (!logged) {
      this.router.navigate(['/']);
      return false;
    }
    return true;
  }

  private async isAuthenticated() {
    return await this.http
      .get<User>('/api/user', { observe: 'response' })
      .toPromise()
      .then(res => {
        if (res.status === 200) {
          this.user = res.body;
          return true;
        }
        return false;
      })
      .catch(() => false);
  }
}
