<template>
    <ul class="search-header">
        <li class="search-row">
            <label>名前：</label>
            <input type="text" name="name" @change="changeValue()">
            <label>分類：</label>
            <select name="classification" @change="changeValue()" v-model="classification">
                <option v-for="list in types" :value="list" v-text="list"></option>
            </select>
            <label>カロリー：</label>
            <input type="text" name="kcal" @change="changeValue()">
        </li>
    </ul>
</template>

<script>
    export default {
        data() {
            return {
                types: [
                    '主菜', '副菜', '主食', 'デザート', 'その他',
                ],
                name: '',
                classification: '',
                kcal: 0,
            }
        },
        methods: {
            changeValue() {
                const params = {
                    name: this.name,
                    classification: this.classification,
                    kcal: this.kcal,
                };
                this.$emit('search', params);
            },
        },
    };
</script>
