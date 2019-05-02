import { AfterViewInit, Component } from '@angular/core';
import { BlockUIService } from './services/blockui.service';

declare var require: any;

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
      this.blockUI.unBlock();
    }, 1000);
  }
}
