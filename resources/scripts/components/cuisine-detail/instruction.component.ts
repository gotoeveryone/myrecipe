import { Component, Input } from '@angular/core';
import { Instruction } from '../../types';

declare var require: any;

/**
 * 調理手順コンポーネント
 */
@Component({
  selector: '[instructions]',
  template: require('./instruction.component.html'),
})
export class InstructionComponent {
  @Input() public items: Instruction[];

  public addRow() {
    this.items.push({});
  }

  public deleteRow() {
    this.items.pop();
  }

  public getOrder(_item: any) {
    if (!_item.sort_order) {
      _item.sort_order = this.items.length;
    }
    return `${_item.sort_order}：`;
  }
}
