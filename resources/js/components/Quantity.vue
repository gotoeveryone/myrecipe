<template>
    <div class="menu-quantity">
        <div class="center">
            <button type="button" class="btn-add" @click="addRow()">追加</button>
            <button type="button" class="btn-delete" @click="deleteRow()">削除</button>
        </div>
        <ul class="quantities">
            <li v-for="quantity in quantities">
                <input type="text" v-model="quantity.foodstuff.name">
                <input type="text" v-model="quantity.detail">
                <select v-model="quantity.foodstuff.classification">
                    <option v-for="classification in classifications" v-text="classification"></option>
                </select>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        data: () => {
            return {
                classifications: [
                    '野菜', '肉', '調味料', '魚', 'デザート',
                ],
            };
        },
        props: ['quantities'],
        methods: {
            addRow() {
                this.quantities.push({
                    foodstuff: {},
                });
            },
            deleteRow() {
                this.quantities.pop();
            },
            getFoodstuffName(_quantity) {
                return _quantity.foodstuff ? _quantity.foodstuff.name : '';
            },
            getClassification(_quantity) {
                return _quantity.foodstuff ? _quantity.foodstuff.classification : '';
            },
        },
    };
</script>