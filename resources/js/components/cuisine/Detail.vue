<template>
    <div class="content-inner">
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
            <instructions :items="cuisine.instructions"></instructions>
            <foodstuffs :items="cuisine.foodstuffs"></foodstuffs>
        </div>
        <div class="footer-button">
            <button type="button" @click="toSearch('cuisine')">検索画面へ</button>
        </div>
        <datalist id="foodstuffs">
            <option v-for="(item, idx) in dataList" :key="idx" :value="item.name"></option>
        </datalist>
    </div>
</template>

<script>
    import Instruction from './Instruction.vue';
    import Foodstuff from './Foodstuff.vue';

    export default {
        props: {
            cuisineId: Number,
        },
        data: () => {
            return {
                cuisine: {
                    instructions: [],
                    foodstuffs: [],
                },
                types: [
                    '主菜', '副菜', '主食', 'デザート', 'その他',
                ],
                dataList: [],
                selectId: 0,
            }
        },
        components: {
            instructions: Instruction,
            foodstuffs: Foodstuff,
        },
        methods: {
            toSearch() {
                location.href = '/recipe/cuisine';
            },
            getLabel() {
                return (this.selectId ? '更新' : '登録');
            },
            getUrl(_type) {
                _type = _type.toUpperCase();
                switch (_type) {
                    case 'GET':
                    case 'PUT':
                    case 'DELETE':
                        return `/recipe/api/cuisine/${this.selectId}/`;
                    case 'POST':
                        return `/recipe/api/cuisine/`;
                }
                return '';
            },
            save() {
                if (this.selectId) {
                    this.$http.put(this.getUrl('put'), JSON.stringify(this.cuisine)).then((data) => {
                        this.cuisine = data.body;
                        this.$emit('dialog', {
                            title: 'メッセージ',
                            message: '料理を更新しました。',
                        });
                    }).catch((s, a, v) => {
                        console.log(s, a, v);
                    });
                } else {
                    this.$http.post(this.getUrl('post'), JSON.stringify(this.cuisine)).then((data) => {
                        this.cuisine = data.body;
                        this.selectId = this.cuisine.id;
                        this.$emit('dialog', {
                            title: 'メッセージ',
                            message: '料理を登録しました。',
                        });
                    }).catch((s, a, v) => {
                        console.log(s, a, v);
                    });
                }
            }
        },
        created() {
            // レシピを取得
            if (this.cuisineId) {
                this.selectId = this.cuisineId;
                this.$http.get(this.getUrl('get')).then((data) => {
                    this.cuisine = data.body;
                });
            }
            // 食材の補完情報を取得
            this.$http.get('/recipe/api/foodstuffs/').then((data) => {
                this.dataList = data.body;
            });
        },
        mounted() {
            if (!this.selectId) {
                for (let i = 0; i < 3; i++) {
                    this.cuisine.instructions.push({
                        sort_order: i + 1,
                    });
                    this.cuisine.foodstuffs.push({});
                }
            }
        }
    };
</script>
