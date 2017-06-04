<template>
    <div class="menu-cooking">
        <div class="center">
            <button type="button" class="btn-add" @click="addRow()">追加</button>
            <button type="button" class="btn-delete" @click="deleteRow()">削除</button>
        </div>
        <ul class="cookings">
            <li v-for="instruction in instructions">
                <span class="cooking-order" v-text="getOrder(instruction)"></span>：
                <input type="text" name="instructions.description" v-model="instruction.description" class="cooking-description">
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        data: () => {
            return {
            }
        },
        props: ['instructions'],
        methods: {
            addRow() {
                console.log(this.instructions);
                this.instructions.push({});
            },
            deleteRow() {
                this.instructions.pop();
            },
            getOrder(_instruction) {
                if (!_instruction.sort_order) {
                    _instruction.sort_order = this.instructions.length;
                }
                return _instruction.sort_order;
            },
        },
    };
</script>