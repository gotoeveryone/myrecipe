require('./bootstrap');

new Vue({
    delimiters: ['${', '}'],
    data: {
        id: '',
        cuisine: {},
    },
    components: {
        instructions: {
            props: ['instructions'],
            template: `
                <ul class="cookings">
                    <li v-for="instruction in instructions">
                        <span class="cooking-order" v-text="getSortOrder(instruction)"></span>：
                        <input type="text" name="instructions.description" v-model="instruction.description" class="cooking-description">
                    </li>
                </ul>
            `,
            methods: {
                getSortOrder(_instruction) {
                    if (!_instruction.sort_order) {
                        _instruction.sort_order = this.instructions.length;
                    }
                    return _instruction.sort_order;
                },
            },
        },
        quantities: {
            props: ['quantities'],
            data() {
                return {
                    classifications: [
                        '野菜',
                        '肉',
                        '調味料',
                        '魚',
                    ],
                };
            },
            template: `
                <ul class="quantities">
                    <li v-for="quantity in quantities">
                        <input type="text" name="quantities.foodstuff.name" v-model="getFoodstuffName(quantity)">
                        <input type="text" name="quantities.detail" v-model="quantity.detail">
                        <select name="quantities.foodstuff.classification" v-model="quantity.foodstuff.classification">
                            <option v-for="classification in classifications" v-text="classification"></option>
                        </select>
                    </li>
                </ul>
            `,
            methods: {                
                getFoodstuffName(_quantity) {
                    return _quantity.foodstuff ? _quantity.foodstuff.name : '';
                },
            },
        }
    },
    methods: {
        toTop: function() {
            location.href = '/';
        },
        toMenu: function() {
            location.href = '/recipe/menu/';
        },
        addRow(_key) {
            this.cuisine[_key].push({});
        },
        deleteRow(_key) {
            this.cuisine[_key].pop();
        },
        save() {
            console.log('ポストされたぜ！！！');
            console.log(JSON.stringify(this.cuisine));
            this.$http.put('/recipe/api/cuisine/1/', JSON.stringify(this.cuisine)).then((data) => {
                this.cuisine = data.body;
            }).catch((s, a, v) => {
                console.log(s, a, v);
            });
        }
    },
    mounted: function() {
        this.$http.get('/recipe/api/cuisine/1/').then((data) => {
            this.cuisine = data.body;
        });
    },
}).$mount('[cuisine]');
