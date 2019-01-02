import { Injectable } from '@angular/core';
import { Http } from '@angular/http';
import { CanActivate, Router } from '@angular/router';

interface IUser {
    account: string;
    name: string;
    email: string;
}

/**
 * 認証状態をチェックするためのサービス
 */
@Injectable()
export class AuthGuardService implements CanActivate {
    private user: IUser;

    constructor(
        private http: Http,
        private router: Router,
    ) { }

    getUser() {
        return this.user;
    }

    clearUser() {
        this.user = null;
    }

    hasUser() {
        return this.user && this.user.account.length > 0;
    }

    async canActivate(): Promise<boolean> {
        const logged = await this.isAuthenticated();
        if (!logged) {
            this.router.navigate(['/']);
            return false;
        }
        return true;
    }

    private async isAuthenticated() {
        return await this.http.get('/api/user')
            .toPromise()
            .then((res) => {
                if (res.status === 200) {
                    this.user = res.json();
                    return true;
                }
                return false;
            })
            .catch((_) => false);
    }
}
