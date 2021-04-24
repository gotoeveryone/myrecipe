import { Component, Input } from '@angular/core';
import { Foodstuff } from '../../types';

declare const require: any;

/**
 * 食材コンポーネント
 */
@Component({
  selector: '[foodstuffs]',
  template: require('./foodstuff.component.html'),
})
export class FoodstuffComponent {
  @Input() public items: Foodstuff[];

  public addRow() {
    this.items.push({});
  }

  public deleteRow() {
    this.items.pop();
  }
}
