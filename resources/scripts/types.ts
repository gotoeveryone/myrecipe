export interface Token {
  token: string;
}

export interface Instruction {
  id?: number;
  sort_order?: number;
  description?: string;
}

export interface Foodstuff {
  id?: number;
  name?: string;
  quantity?: number;
}

export interface Cuisine {
  id?: number;
  instructions: Instruction[];
  foodstuffs: Foodstuff[];
}

export interface Classification {
  id: number;
  name: string;
}
