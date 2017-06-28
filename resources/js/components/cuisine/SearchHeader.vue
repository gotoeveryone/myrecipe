<template>
    <ul class="search-header">
        <li class="search-row">
            <label>名前：</label>
            <input type="text" name="name" @change="changeValue($event)">
            <label>分類：</label>
            <select name="classification" @change="changeValue($event)" v-model="classification">
                <option v-for="(list, idx) in types" :key="idx" :value="list" v-text="list"></option>
            </select>
            <label>カロリー：</label>
            <input type="text" name="kcal" @change="changeValue($event)">以下
        </li>
    </ul>
</template>

<script>
    export default {
        data() {
            return {
                types: [
                    '', '主菜', '副菜', '主食', 'デザート', 'その他',
                ],
                name: '',
                classification: '',
                kcal: 0,
            }
        },
        methods: {
            changeValue($event) {
                this.$emit('search', {
                    [$event.target.name]: $event.target.value,
                });
            },
        },
    };
</script>
