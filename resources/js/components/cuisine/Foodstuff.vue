<template>
    <div class="menu-items">
        <div class="center">
            <button type="button" class="btn-add" @click="addRow()">追加</button>
            <button type="button" class="btn-delete" @click="deleteRow()">削除</button>
        </div>
        <ul class="foodstuffs">
            <li v-for="(item, idx) in items" :key="idx">
                <input type="text" v-model="item.name" list="foodstuffs">
                <input type="text" v-model="item.quantity">
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        data: () => {
            return {
            };
        },
        props: ['items'],
        methods: {
            addRow() {
                this.items.push({});
            },
            deleteRow() {
                this.items.pop();
            },
        },
    };
</script>
