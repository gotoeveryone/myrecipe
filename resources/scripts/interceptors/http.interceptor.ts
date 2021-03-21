import { Injectable } from '@angular/core';
import {
  HttpEvent,
  HttpInterceptor,
  HttpHandler,
  HttpRequest,
  HTTP_INTERCEPTORS,
} from '@angular/common/http';
import { Observable } from 'rxjs';
import { finalize } from 'rxjs/operators';
import { BlockUIService } from '../services/blockui.service';

/**
 * カスタムHTTPモジュール
 */
@Injectable()
export class MyHttpInterceptor implements HttpInterceptor {
  public constructor(
    private blockUI: BlockUIService,
  ) { }

  public intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const newReq = req.clone({
      headers: req.headers
        .set('Authorization', `Bearer ${localStorage.getItem('ACCESS_TOKEN')}`),
    });
    this.blockUI.block();
    return next.handle(newReq).pipe(finalize(() => this.blockUI.unblock()));
  }
}

export function provideHttpInterceptors() {
  return [
    { provide: HTTP_INTERCEPTORS, useClass: MyHttpInterceptor, multi: true },
  ];
}
