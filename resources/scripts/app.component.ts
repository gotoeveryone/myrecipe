import { AfterViewInit, Component } from '@angular/core';
import { BlockUIService } from './services/blockui.service';

declare const require: any;

/**
 * レシピ検索コンポーネント
 */
@Component({
  selector: '.app',
  template: require('./app.component.html'),
})
export class AppComponent implements AfterViewInit {
  public constructor(private blockUI: BlockUIService) {}

  public ngAfterViewInit() {
    setTimeout(() => {
      this.blockUI.unblock();
    }, 1000);
  }
}
