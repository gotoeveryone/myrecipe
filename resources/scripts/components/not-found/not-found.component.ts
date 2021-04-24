import { Component } from '@angular/core';

declare let require: any;

/**
 * 404コンポーネント
 */
@Component({
  selector: '.not-found',
  template: require('./not-found.component.html'),
})
export class NotFoundComponent { }
