//
// Created by 29715 on 2022/4/8.
//


class Bitset {
public:
    string s, s2;
    int _one;
    int _flip;

    Bitset(int size) {
        s.resize(size, '0');
        s2.resize(size, '1');
        _one = 0;
        _flip = false;
    }

    void fix(int idx) {
        if (s[idx] == '0' && !_flip ){
            s[idx] = '1';
            s2[idx] = '0';
            _one += 1;
        }
        else if  (s[idx] == '1' && _flip ){
            s[idx] = '0';
            s2[idx] = '1';
            _one += 1;
        }
    }

    void unfix(int idx) {
        if (s[idx] == '1' && !_flip ){
            s[idx] = '0';
            s2[idx] = '1';
            _one -= 1;
        }
        else if  (s[idx] == '0' && _flip ){
            s[idx] = '1';
            s2[idx] = '0';
            _one -= 1;
        }
    }

    void flip() {
        _flip = !_flip;
        _one = s.size() - _one;
    }

    bool all() {
        if(_flip){
            return _one == 0;
        } else{
            return _one == s.size();
        }
    }

    bool one() {
        if(_flip){
            return _one < s.size();
        } else{
            return _one > 0;
        }
    }

    int count() {
        if(_flip){
            return s.size() - _one;
        } else{
            return _one;
        }
    }

    string toString() {
        if (_flip){
            return s2;
        }else{
            return s;
        }
    }
};



int main() {
    auto b = Bitset(1);
    b.fix(0);
    b.flip();
    cout << b._one << b._flip << b.s << b.s2;
    b.fix(0);
    b.flip();
    cout << b._one << b._flip << b.s << b.s2;
}