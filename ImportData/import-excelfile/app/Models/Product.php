<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Product extends Model
{
    use HasFactory;

    public function tractorType()
    {
        return $this->hasMany(Lookup_data::class,'id', 'tractor_type_id');
    }
}
