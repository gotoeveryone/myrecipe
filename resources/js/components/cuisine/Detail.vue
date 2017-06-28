<template>
    <div>
        <div class="menu-detail">
            <label>名前：</label>
            <input type="text" name="name" v-model="cuisine.name">
            <label>種類：</label>
            <select name="classification" v-model="cuisine.classification">
                <option v-for="(list, idx) in types" :key="idx" :value="list" v-text="list"></option>
            </select>
            <label>Kcal：</label>
            <input type="text" v-model="cuisine.ingestion_kcal">
            <label>種類：</label>
            <input type="text" v-model="cuisine.create_number_of_times">
            <div class="button-wrap">
                <button type="button" @click="save()" class="btn btn-default" v-text="getLabel()"></button>
                <button type="button" class="btn btn-default">メール送信</button>
            </div>
        </div>
        <div class="menu-detail-other">
            <instructions :instructions="cuisine.instructions"></instructions>
            <quantities :quantities="cuisine.quantities"></quantities>
        </div>
        <div class="footer-button">
            <button type="button" @click="toSearch('cuisine')">検索画面へ</button>
            <button type="button" @click="$emit('menu')">メニューへ</button>
        </div>
    </div>
</template>

<script>
    import Instruction from './Instruction.vue';
    import Quantity from './Quantity.vue';

    export default {
        props: {
            cuisineId: Number,
        },
        data: () => {
            return {
                cuisine: {
                    instructions: [],
                    quantities: [],
                },
                types: [
                    '主菜', '副菜', '主食', 'デザート', 'その他',
                ],
            }
        },
        components: {
            instructions: Instruction,
            quantities: Quantity,
        },
        methods: {
            toSearch() {
                location.href = '/recipe/cuisine';
            },
            getLabel() {
                return (this.cuisineId ? '更新' : '登録');
            },
            getUrl(_type) {
                _type = _type.toUpperCase();
                switch (_type) {
                    case 'GET':
                    case 'PUT':
                    case 'DELETE':
                        return `/recipe/api/cuisine/${this.cuisineId}/`;
                    case 'POST':
                        return `/recipe/api/cuisine/`;
                }
                return '';
            },
            save() {
                if (this.cuisineId) {
                    this.$http.put(this.getUrl('put'), JSON.stringify(this.cuisine)).then((data) => {
                        this.title = 'メッセージ';
                        this.message = 'レシピを更新しました。';
                        this.cuisine = data.body;
                    }).catch((s, a, v) => {
                        console.log(s, a, v);
                    });
                } else {
                    this.$http.post(this.getUrl('post'), JSON.stringify(this.cuisine)).then((data) => {
                        this.title = 'メッセージ';
                        this.message = 'レシピを登録しました。';
                        this.cuisine = data.body;
                    }).catch((s, a, v) => {
                        console.log(s, a, v);
                    });
                }
            }
        },
        created() {
            // レシピを取得
            if (this.cuisineId) {
                this.$http.get(this.getUrl('get')).then((data) => {
                    this.cuisine = data.body;
                });
            }
        },
        mounted() {
            if (!this.cuisineId) {
                for (let i = 0; i < 3; i++) {
                    this.cuisine.instructions.push({
                        sort_order: i + 1,
                    });
                    this.cuisine.quantities.push({
                        foodstuff: {},
                    });
                }
            }
        }
    };
</script>
