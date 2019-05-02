import { Injectable } from '@angular/core';

/**
 * 画面のブロックを制御するためのサービス
 */
@Injectable()
export class BlockUIService {
  private showBlock = true;

  public get blocked() {
    return this.showBlock;
  }

  public block() {
    this.showBlock = true;
  }

  public unBlock() {
    this.showBlock = false;
  }
}
