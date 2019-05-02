import { Component, Input } from '@angular/core';

declare var require: any;

/**
 * 食材コンポーネント
 */
@Component({
  selector: '[foodstuffs]',
  template: require('./foodstuff.component.html'),
})
export class FoodstuffComponent {
  @Input() public items: any[];

  public addRow() {
    this.items.push({});
  }

  public deleteRow() {
    this.items.pop();
  }
}
